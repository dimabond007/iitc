document.addEventListener('DOMContentLoaded', () => {
    const sentence = "Where you go I follow, no matter how far. If life is a movie, oh you're the best part.".toUpperCase();
    const livesCount = document.getElementById('livesCount');
    const mistakesCount = document.getElementById('mistakesCount');
    let lives = 3;
    let mistakes = 0;

    const letterToNumber = new Map();
    let nextNumber = 1;

    // Присваиваем каждой букве число
    for (const letter of sentence) {
        if (!letterToNumber.has(letter) && letter !== ' '&& letter !== '.') {
            letterToNumber.set(letter, nextNumber++);
        }
    }

    // Функция для создания игрового поля
    function createGameBoard(sentence) {
        const gameBoard = document.getElementById('gameBoard');
        gameBoard.innerHTML = ''; // Очистка доски

        for (const letter of sentence) {
            const button = document.createElement('button');

            if (letter === ' ') {
                button.textContent = ' ';
                button.disabled = true;
                button.className = 'space';
            }
            else if (letter === '.') {
                button.textContent = '.';
                button.disabled = true;
                button.className = 'space';
            } 
            else {
                button.textContent = letterToNumber.get(letter).toString();
                button.className = 'number';
                button.onclick = function() { attempt(letter, button); };
            }

            gameBoard.appendChild(button);
        }
    }

    // Обработка попытки
    function attempt(letter, button) {
        if (button.textContent === letterToNumber.get(letter).toString()) {
            button.textContent = letter;
            button.disabled = true;
            button.className = 'letter';
            // Проверка, завершена ли игра
            checkCompletion();
        } else {
            mistakes++;
            mistakesCount.textContent = mistakes.toString();
            if (mistakes === 3) {
                endGame(false);
            }
        }
    }

    // Проверка, все ли буквы отгаданы
    function checkCompletion() {
        const allGuessed = Array.from(document.querySelectorAll('.number')).every(btn => btn.disabled);
        if (allGuessed) {
            endGame(true);
        }
    }

    // Завершение игры
    function endGame(win) {
        const gameBoard = document.getElementById('gameBoard');
        gameBoard.innerHTML = win ? 'Вы выиграли!' : 'Вы проиграли!';
    }

    createGameBoard(sentence);
});
