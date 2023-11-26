const postData = async (url = '', data = {}) => {
        // Формируем запрос
        const response = await fetch(url, {
            // Метод, если не указывать, будет использоваться GET
            method: 'POST',
        // Заголовок запроса
            headers: {
            'Content-Type': 'application/json'
            },
            // Данные
            body: JSON.stringify(data)
        });
        return response.json();
        }
        const send = () => {
            postData('/NewPost', { answer: 42 }).then((data) => {
                console.log(data);
            });
        }