$(function(){
    let categories = $('div[data-step=\'1\'] div label input');
    let institutionCategories = $('div[data-step=\'3\'] div  div[data-category]');
    let stepThree = $('div[data-step=\'2\'] .next-step');

    // console.log(institutionCategories);

    function checkIfContains(categoryName, categoryList) {
        let contains = false;
        for(let i=0; i<categoryList.length; i++){
            if(categoryName === categoryList[i]){
                contains = true;
            }
        }
        return contains;
    }

    stepThree.click(function(){
        for(let j=0; j<institutionCategories.length; j++){
            $(institutionCategories[j]).parent().show();
        }

        for(let i=0; i<categories.length; i++) {
            if (categories[i].checked) {
                let categoryName = categories[i].getAttribute('value');
                for(let j=0; j<institutionCategories.length; j++){
                    let categoryList = institutionCategories[j].getAttribute('data-category').split('; ');
                    if(!checkIfContains(categoryName, categoryList)){
                        $(institutionCategories[j]).parent().hide();
                    }
                }
            }
        }
    });
});