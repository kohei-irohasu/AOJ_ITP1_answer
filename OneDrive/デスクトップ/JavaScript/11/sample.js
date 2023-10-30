// window.alert('アラートです');
// const result = confirm('本当に削除してもよいですか');
// if (result) {
//     console.log('削除しました');
// } else {
//     console.log('キャンセルしました');
// }

// function delayTask () {
//     console.log('1秒ごとに繰り返し実行される');
// }
// const timerId = setInterval(delayTask, 1000);
// clearInterval(timerId);

// const newWindow1 = open('https://example.com');

// newWindow1.close();

// const tag = window.document.querySelector('#sample');
// tag.textContent = 'テキストを書き換えます';

// const element = document.querySelector('.sample');
// console.log(element);

// const elements = document.querySelectorAll('.sample');
// // // console.log(elements.length);
// // console.log(elements);

// const elements = document.querySelectorAll('.sample');
// // for (const element of elements) {
// //     console.log(element);
// // }
// console.log(elements[1]);

// const p = document.querySelector('p');
// // p.textContent = '変更します';
// p.style.fontSize = '36px';

// // const img = document.querySelector('img');
// // img.width = 300;

// const profile = document.querySelector('.profile');
// // console.log(profile.dataset.id);
// // console.log(profile.dataset.userName);
// profile.dataset.id = 999;
// profile.dataset.userName = 'new zaru';
// console.log(profile);

// const ScoreElement = document.querySelector('.score');
// const score = ScoreElement.dataset.score;
// if (score >= 80) {
//     ScoreElement.style.color = 'blue';
// }

// // const element1 = document.querySelector('p');
// // // element1.classList.remove('normal');
// element.classList.add('warning');

// const element = document.querySelector('p');
// element.classList.replace('normal', 'warning');

// const element = document.createElement('p');
// console.log(element);

// const newElement = document.createElement('p');
// newElement.textContent = '新しく追加しました';
// const content = document.querySelector('.content');
// content.append(newElement);

// const newElement = document.createElement('p');
// // newElement.textContent = '先頭に追加したい';
// // const content = document.querySelector('.content');
// content.prepend(newElement);

// const newElement = document.createElement('p');
// newElement.textContent = '新しく追加しました';
// const firstElement = document.querySelector('.first');
// firstElement.before(newElement);


// const firstElement = document.querySelector('.first');
// firstElement.remove();

// const newElement = document.createElement('p');
// newElement.textContent = '置き換えの要素';

// const firstElement = document.querySelector('.first');
// firstElement.replaceWith(newElement);

// function alertMessage() {
//     alert('ボタンをクリックしました');
// // // // }

// const button = document.querySelector('button');
// button.addEventListener('click', function () {
//     alert('ボタン！ボタン！');
// });

// // function event () {
// //     console.log('関数名が特定できるので削除可能')
// }
// button.addEventListener('click', event);
// button.removeEventListener('click', event);

// const input = document.querySelector('input');
// input.addEventListener('input', function (event) {
//     const value = event.currentTarget.value;
//     console.log(`入力内容: ${value}`);
// });

const radios = document.querySelectorAll('.radio');
for (let radio of radios) {
    radio.addEventListener('input', function (event) {
        const value = event.currentTarget.value;
        console.log(`${value}がチェックされました`);
    });
}

// const checkboxes = document.querySelectorAll('.checkbox');
// checkboxes.addEventListener('input', function (event) {
//     const value = event.currentTarget.value;
//     console.log(`${value}がチェックされました`);
// });

const select = document.querySelector('.select');
select.addEventListener('input', function(event) {
    const value = event.currentTarget.value;
    console.log(`${value}が選択されました`);
});


const input = document.querySelector('input');
input.addEventListener('keydown', function (event) {
    console.log(event.key);
});

const div = document.querySelector('div');
div.addEventListener('mousemove', function (event) {
    console.log(`Move : x = ${event.offsetX}, y = ${event.offsetY}`);
});
div.addEventListener('mousedown', function (event) {
    console.log(`Down : x = ${event.offsetX}, y= ${event.offsetY}`);
});
div.addEventListener('mouseup', function (event) {
    console.log(`Up : x = ${event.offsetX}, y = ${event.offsetY}`);
});

// const scrollContent = document.querySelector('.scroll');
// for(let i = 0; i < 1000; i++) {
//     scrollContent.textContent += `テキスト${i}`;
// }
// window.addEventListener('scroll', function () {
//     console.log(`スクロール量は${window.scrollY}pxです`);
// });

const button = document.querySelector('button');
button.addEventListener('click', function (event) {
    const button = event.currentTarget;
    button.textContent = '変更します';
});

function confirmLink(event) {
    if (confirm('ページを遷移しますか？')) {
        console.log('実行しました')
    } else {
        console.log('キャンセルしました');
        event.preventDefault();
    }
}

const link = document.querySelector('a');
link.addEventListener('click', confirmLink);


// function syncAlert() {
//     alert('アラートを表示');
//     console.log('ログを出力');
// }
// syncAlert()

function asyncAlert() {
    setTimeout(function () {
        alert('アラートを表示');
    }, 0);
    console.log('ログを出力');
}

asyncAlert()
