function togglePasswordVisibility(passwordId, toggleIconId) {
    var passwordInput = document.getElementById(passwordId);
    var toggleIcon = document.getElementById(toggleIconId);

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        toggleIcon.classList.remove('fa-eye');
        toggleIcon.classList.add('fa-eye-slash');
    } else {
        passwordInput.type = "password";
        toggleIcon.classList.remove('fa-eye-slash');
        toggleIcon.classList.add('fa-eye');
    }
}