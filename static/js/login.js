;
var login = {
    init:function(){
        this.eventBind();
    },

    eventBind:function(){
        $(".login-form .login-button").click( function() {
                var login_name = $(".login-form input[name=input-email]").val();
                var login_pwd = $(".login-form input[name=input-pwd]").val();

                if ( login_name == null ) {
                    alert("No user name found");
                    return ;
                };

                if ( login_pwd == null || login_name.len < 6 ) {
                    alert("No password found");
                    return ;
                };

                // alert(login_name);


        })
    }
};

$(document).ready( function() {
    login.init();
})