const books = document.querySelectorAll('.book');
const subpage = document.getElementById('subpage');
const bookContent = document.getElementById('book-content');
const closeBtn = document.querySelector('.close-btn');

books.forEach(book => {
    const cover = book.querySelector('.cover');
    const title = book.querySelector('.title').textContent;
    const content = book.querySelector('.content').innerHTML;

    cover.addEventListener('click', () => {
        bookContent.innerHTML = `
        <div style="font-family: 'Uni Sans Heavy Regular', sans-serif; font-size: 16px; text-align: center;">${title}</div>
        ${content}
    `;
        subpage.style.display = 'flex';
    });
});

closeBtn.addEventListener('click', () => {
    subpage.style.display = 'none';
});

subpage.addEventListener('click', (e) => {
    if (e.target === subpage) {
        subpage.style.display = 'none';
    }
});