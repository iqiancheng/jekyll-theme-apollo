document.addEventListener('DOMContentLoaded', function () {
    var codeBlocks = document.querySelectorAll('div.highlighter-rouge');

    codeBlocks.forEach(function (block) {
        // Create copy button
        var button = document.createElement('button');
        button.className = 'copy-code-btn';
        button.innerHTML = '<i class="fa fa-copy"></i> Copy'; // You might need FontAwesome or just text
        button.textContent = 'Copy';

        // Add click event
        button.addEventListener('click', function () {
            var code = block.querySelector('code').innerText;
            navigator.clipboard.writeText(code).then(function () {
                button.textContent = 'Copied!';
                setTimeout(function () {
                    button.textContent = 'Copy';
                }, 2000);
            }, function (err) {
                console.error('Failed to copy: ', err);
            });
        });

        // Append button to the block
        block.appendChild(button);
    });
});
