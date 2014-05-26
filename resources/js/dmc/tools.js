function maskBegin(message) {
    $('#maskMessage').html(message + ' ......');
    $('#maskLoad').window('open');
    //alert('In maskBegin');
    //$.messager.progress({
    //    title: 'Please waiting',
    //    //msg: 'Loading data...',
    //    text: message + ' .......',
    //	style:{	right:'',
    //			bottom:''
    //		  }
    //});

    //$("<div class=\"datagrid-mask\"></div>").css({display:"block",width:"100%",height:$(window).height()}).appendTo("body");
    //$("<div class=\"datagrid-mask-msg\"></div>").html("Loading ......").appendTo("body").css({display:"block",left:($(document.body).outerWidth(true) - 190) / 2,top:($(window).height() - 45) / 2});
}

function maskEnd() {
    $('#maskLoad').window('close');
    //return
    //alert('In maskEnd');
    //$.messager.progress('close');
    //$(".datagrid-mask").remove();
    //$(".datagrid-mask-msg").remove();
}