;
var login = {
    init:function(){
        this.eventBind();
    },

    eventBind:function(){
        $(".login-form .login-button").click( function() {
                var login_name = $(".login-form input[name=input-email]").val();
                var login_pwd = $(".login-form input[name=input-pwd]").val();

                alert(login_name);
                alert(login_pwd);
                if ( login_name = undefined || login_name.len < 1 ) {
                    alert("No user name found");
                };

                if ( login_pwd = undefined || login_name.len < 1 ) {
                    alert("No password found");
                };


        })
    }
};

$(document).ready( function() {
    login.init();
})