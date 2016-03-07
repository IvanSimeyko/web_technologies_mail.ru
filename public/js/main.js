function showText (el) {
    console.log(el);
    if (el.previousElementSibling.clientHeight === 80) {
        el.previousElementSibling.style.height = '100%';
        el.innerHTML = 'Sow less...';
    } else {
        el.previousElementSibling.style.height = '80px';
        el.innerHTML = 'Read more...';
    }
}