String.prototype.contains = function contains(match) { return this.indexOf(match) !== -1; }

var PageController = function() {
    var self = this;

    self.data = {};
    self.data.api = {};
    self.data.api.version = 'v1';
    self.data.api.base = window.location.origin + '/' + self.data.api.version + '/';
    self.data.token = undefined;
    self.data.aws = {};
    self.data.aws.bucket = 'bieraustin';
    self.data.aws.album = 'beerfridge/';
    self.data.beers = {results: []}
    self.data.breweries = {results: []}
    self.data.options = {}
    self.data.lookup = {}
    self.data.lookup.breweries = {}
    self.data.lookup.locations = {}
    self.data.lookup.glassware = {}
    self.data.glasswares = {results: []}
    self.data.locations = {results: []}
    self.data.params = { 'ordering': '', };

    self.s3 = new AWS.S3({
                        apiVersion: '2006-03-01',
                        params: {Bucket: self.data.aws.bucket}
                    });

    self.lock = new Auth0Lock(AUTH0_CLIENT_ID, AUTH0_DOMAIN, {
        auth: { params: { scope: 'openid email' } }
    });

    self.target = {};
    self.target.content = $('#content');
    self.target.navbar = $('#navbar');
    self.target.profile = $('#profile');

    self.template = {};
    self.template.home = $('#template-home').html();
    self.template.beers = $('#template-beers').html();
    self.template.breweries = $('#template-breweries').html();
    self.template.locations = $('#template-locations').html();
    self.template.glasswares = $('#template-glasswares').html();
    self.template.errors = '<ul class="list-unstyled"><% _.each(errors, function(error, field) { %><li><%= field %>: <%= error %></li><% }); %></ul>';

    self.template.logged_in = '<li class="profile"> <img class="img-rounded profile-img" alt="avatar" src="<%= profile.picture %>" /> <span class="nickname"><%= profile.nickname %></span> </li> <li><a class="link logout">Sign Out</a> </li>';
    self.template.logged_out = '<li><a class="link login">Sign In</a></li>';

    var init = function() {
        $(document).on('click', 'a:not(".link")', function(el) {
            el.preventDefault();
            window.location.hash = this.hash;
            self.page.set();
            self.render.page();
        });

        $(document).on('click', '.link.ordering', function(el) {
            link = $(this);
            splitter = window.location.hash.contains('/?') ? '/?' : '?';
            hash = window.location.hash.split(splitter);
            window.location.hash = hash[0] + '/?ordering=' + link.data('field');
            self.page.set();
            self.render.page();
        });

        $(document).on('click', '.link.toggle', function(el) {
            var link = $(this);
            link.find('.btn').removeClass('hide');
            link.removeClass('glyphicon-chevron-right');
        });

        $(document).on('click', '.btn.delete', function(el) {
            var link = $(this);
            $.ajax({
                url: self.data.api.base + link.data('uri'),
                method: 'DELETE',
                success: function(result) {
                    link.closest('.card').hide();
                }
            });
        });

        $(document).on('submit', 'form', function(el) {
            el.preventDefault();
            form = $(this);
            var data = form.serializeObject();

            uploads = form.find('input[type=file]');
            for (i=0; i < uploads.length; i++) {
                field = uploads[i];
                if (field.files.length) {
                    key = 'id' in data ? data.id : ('name' in data ? data.name : guid());
                    data[$(field).prop('name')] = self.upload(field.files[0], key);
                }
            }

            var result_field = form.find('.result');
            result_field.removeClass('hide alert-success alert-danger').html('');
            $.ajax({
                url: form.prop('action'),
                method: form.prop('method'),
                dataType : 'json',
                data: data,
                success: function(result) {
                    result_field.addClass('alert-success').html('Success!');
                    form[0].reset();
                    self.load.options();
                },
                error: function(result) {
                    result_field.addClass('alert-danger').html(_.template(self.template.errors)({'errors': result.responseJSON}));
                }
            });
        });

        $(document).on('click', '.card.effect__click .flip', function(el) {
            $(this).closest('.card').toggleClass("flipped");
        });

        $('#image-modal').on('show.bs.modal', function (event) {
            var button = $(event.relatedTarget);
            var image = button.data('image');
            var modal = $(this);
            modal.find('.modal-body img').prop('src', image);
        })

        $('#image-upload-modal').on('show.bs.modal', function (event) {
            var button = $(event.relatedTarget);
            var action = button.data('uri');
            var modal = $(this);
            modal.find('.modal-body form').prop('action', action);
        })

        $(document).on('click', '.link.login', function(e) {
            e.preventDefault();
            self.lock.show();
        });

        $(document).on('click', '.link.logout', function(e) {
            e.preventDefault();
            self.auth.logout();
        })

        self.lock.on("authenticated", function(authResult) {
            self.lock.getProfile(authResult.idToken, function(error, profile) {
                if (error) { return; }
                if ('bieraustin@gmail.com' == profile.email) {
                    localStorage.setItem('id_token', authResult.idToken);
                    self.data.profile = profile;
                    self.auth.show();
                }
            });
        });

        self.page.set();
        self.auth.profile();

        self.load.options(self.render.page);
    }

    self.auth = {};

    self.auth.profile = function() {
        token = localStorage.getItem('id_token');
        if (!self.data.profile && token) {
            self.lock.getProfile(token, function (err, profile) {
                if (err) {
                    self.data.profile = undefined;
                    localStorage.removeItem('id_token');
                } else {
                    self.data.profile = profile;
                }
                self.auth.show();
            });
        } else {
            self.auth.show();
        }
    };

    self.auth.show = function() {
        if (self.data.profile) {
            self.target.profile.html(_.template(self.template.logged_in)(self.data));
        } else {
            self.target.profile.html(_.template(self.template.logged_out)(self.data));
        }
        self.render.content();
    };

    self.auth.logout = function() {
        self.data.profile = undefined;
        localStorage.removeItem('id_token');
        self.auth.show();
    };

    self.upload = function(file, key) {
        var photoKey = self.data.aws.album + key;
        s3.upload({
            Key: photoKey,
            Body: file,
            ACL: 'public-read'
        }, function(err, data) {
            if (err) { return err.message; }
            return data.Location;
        });
        return 'https://bieraustin.s3-us-west-2.amazonaws.com/'+photoKey;
    }

    self.page = {};

    self.page.set = function() {
        self.data.path = window.location.hash.replace('#', '');
        splitter = window.location.hash.contains('/?') ? '/?' : '?';
        parts = self.data.path.replace(/\/+$/, '').split(splitter);
        params = parts[parts.length-1].split('&');
        self.data.params = { 'ordering': '', }
        for (i=0; i < params.length; i++) {
            param = params[i].split('=', 2);
            self.data.params[param[0]] = param[1];
        }
        parts = parts[0].split('/');
        self.data.template = parts[parts.length-1];
        if (!(self.data.template in self.template)) { self.data.template = 'home'; }
    }

    self.render = {}
    self.render.nav = function() {
        self.target.navbar.find('li').removeClass('active');
        self.target.navbar.find('li.'+self.data.template).addClass('active');
    }

    self.render.page = function() {
        self.render.nav();
        if ('home' == self.data.template) {
            self.render.content();
        } else {
            self.load.data(self.data.path);
        }
    }

    self.render.content = function() {
        if (self.data.profile) {
            self.target.content.html(_.template(self.template[self.data.template])(self.data));
        } else {
            self.target.content.html('');
        }
    }

    self.load = {};
    self.load.data = function(path) {
        $.getJSON('/v1/'+path, function(data) {
            self.data[self.data.template] = data;
            self.render.content();
        });
    }

    self.load.options = function(callback) {
        $.getJSON('/v1/options', function(data) {
            self.data.options = data;
            _.each(self.data.options.locations, function(l) {
                self.data.lookup.locations[l.id] = l.name;
            });
            _.each(self.data.options.breweries, function(b) {
                self.data.lookup.breweries[b.id] = b.name;
            });
            _.each(self.data.options['glassware-styles'], function(b) {
                self.data.lookup.glassware[b[0]] = b[1];
            });
            if (callback) {
                callback();
            }
        });
    }
    init();
}
PageController();
