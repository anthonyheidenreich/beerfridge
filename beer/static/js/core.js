String.prototype.contains = function contains(match) { return this.indexOf(match) !== -1; }

AWS.config.region = 'us-west-2'; // Region
AWS.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: 'us-west-2:43d6d9cb-2f64-4f07-bb19-d46554d40723',
});

function guid() {
    function s4() {
        return Math.floor((1 + Math.random()) * 0x10000)
            .toString(16)
            .substring(1);
    }
    return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
        s4() + '-' + s4() + s4() + s4();
}


var PageController = function() {
    var self = this;

    self.data = {};
    self.data.api = {};
    self.data.api.version = 'v1';
    self.data.api.base = window.location.origin + '/' + self.data.api.version + '/';
    self.data.aws = {};
    self.data.aws.bucket = 'bieraustin';
    self.data.aws.album = 'beerfridge/';
    self.data.beers = {results: []}
    self.data.breweries = {results: []}
    self.data.options = {}
    self.data.glasswares = {results: []}
    self.data.locations = {results: []}
    self.data.params = {
        'ordering': '',
    };

    self.s3 = new AWS.S3({
                        apiVersion: '2006-03-01',
                        params: {Bucket: self.data.aws.bucket}
                    });


    self.target = {};
    self.target.content = $('#content');
    self.target.navbar = $('#navbar');

    self.template = {};
    self.template.home = $('#template-home').html();
    self.template.beers = $('#template-beers').html();
    self.template.breweries = $('#template-breweries').html();
    self.template.locations = $('#template-locations').html();
    self.template.glasswares = $('#template-glasswares').html();
    self.template.errors = '<ul class="list-unstyled"><% _.each(errors, function(error, field) { %><li><%= field %>: <%= error %></li><% }); %></ul>';

    var init = function() {
        $(document).on('click', 'a', function(el) {
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

        $(document).on('click', '.link.delete', function(el) {
            var link = $(this);
            $.ajax({
                url: self.data.api.base + link.data('uri'),
                method: 'DELETE',
                success: function(result) {
                    link.closest('tr').hide();
                }
            });
        });

        $(document).on('submit', 'form', function(el) {
            el.preventDefault();
            form = $(this);
            var result_field = form.find('.result');
            uploads = form.find('input[type=file]');
            var data = form.serializeObject();
            for (i=0; i < uploads.length; i++) {
                field = uploads[i];
                if (field.files.length) {
                    key = 'id' in data ? data.id : ('name' in data ? data.name : guid());
                    data[$(field).prop('name')] = self.upload(field.files[0], key);
                }
            }
            result_field.removeClass('hide alert-success alert-danger').html('');
            $.ajax({
                url: form.prop('action'),
                method: form.prop('method'),
                dataType : 'json',
                data: data,
                success: function(result) {
                    result_field.addClass('alert-success').html('Success!');
                    form[0].reset();
                },
                error: function(result) {
                    result_field.addClass('alert-danger').html(_.template(self.template.errors)({'errors': result.responseJSON}));
                }
            });
        });

        $('#image-modal').on('show.bs.modal', function (event) {
            var button = $(event.relatedTarget);
            var image = button.data('image');
            var modal = $(this);
            modal.find('.modal-body img').prop('src', image);
        })

        self.page.set();

        $.getJSON('/v1/options', function(data) {
            self.data.options = data;
            $.getJSON('/v1/breweries', function(data) {
                self.data.breweries = data;
                $.getJSON('/v1/locations', function(data) {
                    self.data.locations = data;
                    self.render.page();
                });
            });
        });
    }

    self.upload = function(file, key) {
        var photoKey = self.data.aws.album + key;
        s3.upload({
            Key: photoKey,
            Body: file,
            ACL: 'public-read'
        }, function(err, data) {
            if (err) {
                return err.message;
            }
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
        if (!self.data.template) { self.data.template = 'home'; }
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
        self.target.content.html(_.template(self.template[self.data.template])(self.data));
    }

    self.load = {};
    self.load.data = function(path) {
        $.getJSON('/v1/'+path, function(data) {
            self.data[self.data.template] = data;
            self.render.content();
        });
    }
    init();
}
PageController();
