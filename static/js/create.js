const postData = async (url = '', data) => {
    // Формируем запрос
    const response = await fetch(url, {
      method: 'POST',

      headers: {
        'Content-Type': 'text'
      },
      body: data
    });
    return response.text()
    }

    function send(){
        json ={text: document.getElementById('text')}
        postData('NewPost', JSON.stringify(json))

    }

    const button = document.getElementById('send')
    window.addEventListener("DOMContentLoaded", (event) => {
      const el = document.getElementById('send');
      if (el) {
        el.addEventListener('click', send, false);
      }
  });