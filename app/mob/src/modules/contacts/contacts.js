require('./contacts.less');

var appFunc = require('../utils/appFunc'),
    service = require('./service'),
    template = require('../home/home.tpl.html');

var contacts = {
    init: function(){
        contacts.bindEvents();
    },
    loadContacts: function(){
        console.log('loadContacts');
        if(contacts.beforeLoadContacts()) {
            //hiApp.searchbar('#contactView .searchbar',{
            //    searchList: '.contacts-list',
            //    searchIn: '.item-title'
            //});

            service.loadContacts(function(tl, type){
                setTimeout(function(){
                    //var renderData = {
                    //    contacts: c
                    //};
                    //console.log(renderData);
                    //var output = appFunc.renderTpl(template, renderData);
                    //$$('#contactView .contacts-list ul').html(output);
                    //
                    hiApp.hideIndicator();
                    //var renderData = {
                    //    timeline: tl,
                    //    finalText: function(){
                    //        return appFunc.matchUrl(this.text);
                    //    },
                    //    time: function(){
                    //        return appFunc.timeFormat(this.created_at);
                    //    }
                    //};
                    //var output = appFunc.renderTpl(template, renderData);
                    //if(type === 'prepend'){
                    //    $$('#contactView').find('.home-timeline').prepend(output);
                    //}else if(type === 'append') {
                    //    $$('#contactView').find('.home-timeline').append(output);
                    //}else {
                    //    $$('#contactView').find('.home-timeline').html(output);
                    //}

                    var renderData = {
                        timeline: tl,
                        finalText: function(){
                            return appFunc.matchUrl(this.text);
                        },
                        time: function(){
                            return appFunc.timeFormat(this.created_at);
                        }
                    };
                    var output = appFunc.renderTpl(template, renderData);
                    //$$('#contactView').html(output);
                    $$('#contactView').find('.home-timeline').html(output);
                    //console.log(template);
                    //if(type === 'prepend'){
                    //    $$('#contactView').find('.home-timeline').prepend(output);
                    //}else if(type === 'append') {
                    //    $$('#contactView').find('.home-timeline').append(output);
                    //}else {
                    //    $$('#contactView').find('.home-timeline').html(output);
                    //}


                },500);
            });
        }
    },
    beforeLoadContacts: function(){
        if($$('#contactView .contacts-list .list-group .contact-item').length > 0) {
            return false;
        }else {
            hiApp.showIndicator();
            return true;
        }
    },
    openItemPage: function(e){
        if(e.target.nodeName === 'A' || e.target.nodeName === 'IMG'){
            return false;
        }
        var itemId = $$(this).data('id');
        console.log('page/tweet.html?id=' + itemId);
        homeF7View.router.loadPage('page/tweet.html?id=' + itemId);
    },
    bindEvents: function(){
        var bindings = [{
            element: '#contactView',
            event: 'show',
            handler: contacts.loadContacts
        },
        {
            element: '#contactView',
            selector: '.home-timeline .ks-facebook-card',
            event: 'click',
            handler: this.openItemPage
        }
        ];

        appFunc.bindEvents(bindings);
    }
};

module.exports = contacts;
