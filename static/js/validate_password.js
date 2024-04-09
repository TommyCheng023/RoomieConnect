function validatePassword() {
    /** 
     * Generate a styled alert message once the re-entered password does not match with the initial password.
     * 
     * @returns{bool} Return a boolean value to determine whether the registration form should be submitted or not.
     */
    let pwd1 = document.getElementById('password').value;
    let pwd2 = document.getElementById('rePassword').value;
    let alertMsg = document.getElementById('alert-msg-for-js');
    if(pwd1 === pwd2) {
        alertMsg.style.display = 'none';
        return true;
    }
    else {
        alertMsg.style.display = 'block';
        return false;
    }
}