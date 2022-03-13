const ProductContainer = [...document.querySelectorAll('.product-container')];
const nextBtn = [...document.querySelectorAll('.nextbtn')];
const preBtn = [...document.querySelectorAll('.prebtn')];

ProductContainer.forEach((item, i) => {
    let containDimension = item.getBoundingClientRect();
    let containWidth = containDimension.width;
    
    nextBtn[i].addEventListener('click', () =>{
        item.scrollLeft += containWidth;
    })
    preBtn[i].addEventListener('click', () =>{
        item.scrollLeft -= containWidth;
    })
}) 