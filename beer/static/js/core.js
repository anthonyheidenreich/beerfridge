var PageController = function() {
    var self = this;

    self.data = {};
    self.data.api_base = window.location.origin + '/v1/';

    self.target = {};
    self.target.content = $('#content');
    self.target.navbar = $('#navbar');

    self.template = {};
    self.template.home = $('#template-home').html();
    self.template.beers = $('#template-beers').html();
    self.template.breweries = $('#template-breweries').html();
    self.template.locations = $('#template-locations').html();
    self.template.glasswares = $('#template-glasswares').html();

    var init = function() {
        $(document).on('click', 'a', function(el) {
            el.preventDefault();
            window.location.hash = this.hash;
            self.page.set(this.hash.replace('#', ''));
            self.render.page();
        });

        self.page.set(window.location.hash.replace('#', ''));
        self.render.page();
    }

    self.page = {};

    self.page.set = function(path) {
        self.data.path = path;
        parts = self.data.path.replace(/\/+$/, '').split('/?');
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
