
//for passing text to type
document.addEventListener('DOMContentLoaded', function() {
    // var contentText = '{{ content_text|escapejs }}';
    document.getElementById('content').innerHTML = '<p>' + contentText + '</p>';
});

document.addEventListener('DOMContentLoaded', (event) => {
    let firstKeyPress = false;
    let firstKeypressTimestamp = null;
    const textarea = document.getElementById('textarea');
    const submitBtn = document.getElementById('submit-btn');

    textarea.addEventListener('keydown', function() {
        if (!firstKeyPress) {
            firstKeyPress = true;
            firstKeypressTimestamp = new Date().toISOString();
        }
    });

    submitBtn.addEventListener('click', function() {
        const submitTimestamp = new Date().toISOString();
        const content = textarea.value;

        fetch('', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')  // Include the CSRF token
            },
            body: JSON.stringify({
                first_keypress_timestamp: firstKeypressTimestamp,
                submit_timestamp: submitTimestamp,
                content: content
            })
        })
        .then(response => {
            if (response.redirected) {
                window.location.href = response.url;
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });

    // Function to get CSRF token from cookie
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
