$(function(){
    let categories = $('div[data-step=\'1\'] div label input');
    let institutionCategories = $('div[data-step=\'3\'] div  div[data-category]');
    let stepThree = $('div[data-step=\'2\'] .next-step');

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
                let categoryName = categories[i].getAttribute('data-value');
                for(let j=0; j<institutionCategories.length; j++){
                    let categoryList = institutionCategories[j].getAttribute('data-category').split('; ');
                    if(!checkIfContains(categoryName, categoryList)){
                        $(institutionCategories[j]).parent().hide();
                    }
                }
            }
        }
    });


    let lastStep = $('div[data-step=\'4\'] .next-step');

    lastStep.click(function() {
        let donationBagsInfo = $('.summary--text')[0];
        let donationInstitutionInfo = $('.summary--text')[1];
        let donationDeliveryInfo = $('div[data-step=\'5\'] .form-section--column ul li');

        let bagAmount = $('[name=\'bags\']').val();
        let bagString = '';
        if (bagAmount < 2) {
            bagString = 'worek'
        } else if (bagAmount < 5) {
            bagString = 'worki'
        } else {
            bagString = 'worków'
        }
        let chosenCategories = '';
        for (let i = 0; i < categories.length; i++) {
            if (categories[i].checked) {
                let category = categories[i].getAttribute('data-value');
                chosenCategories += ' ' + category + ',';
            }
        }
        chosenCategories = chosenCategories.substring(0, chosenCategories.length - 1);

        let institutions = $('div[data-step=\'3\'] div label input');
        let chosenInstitution = '';
        for (let i = 0; i < institutions.length; i++) {
            if (institutions[i].checked) {
                chosenInstitution = institutions[i].value;
            }
        }
        donationBagsInfo.innerText = `${bagAmount} ${bagString} o zawartości: ${chosenCategories}.`;
        donationInstitutionInfo.innerText = `Dla: ${chosenInstitution}`;

        donationDeliveryInfo[0].innerText = $('[name=\'address\']').val();
        donationDeliveryInfo[1].innerText = $('[name=\'city\']').val();
        donationDeliveryInfo[2].innerText = $('[name=\'postcode\']').val();
        donationDeliveryInfo[3].innerText = $('[name=\'phone\']').val();
        donationDeliveryInfo[4].innerText = $('[name=\'data\']').val();
        donationDeliveryInfo[5].innerText = $('[name=\'time\']').val();
        donationDeliveryInfo[6].innerText = $('[name=\'more_info\']').val();

    });
});