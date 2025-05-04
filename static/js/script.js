console.log('Javascript loaded...')

document.querySelector('#sendButton').addEventListener('click', async function (e) {
    e.preventDefault();
    const message = document.querySelector('#chatInput').value;
    document.querySelector('#chatInput').value = '';

    // Mensagem do usuário
    // cria um elemento <p> com classe 'user-message' e coloca dentro de #chatMessages
    const userMessageElement = document.createElement('p');
    userMessageElement.className = 'user-message';
    userMessageElement.textContent = message;
    document.querySelector('#chatMessages').appendChild(userMessageElement);

    const response = await fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message }) // {'message': message}
    });

    const data = await response.json();
    if (response.ok) {
        document.querySelector('#chatMessages').insertAdjacentHTML('beforeend', data.html);
    } else {
        console.log(data.error);
        document.querySelector('#chatMessages').insertAdjacentHTML('beforeend', data.error);
    }
});