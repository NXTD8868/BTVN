console.log("Zo");
var rbs = document.getElementsByClassName("remove_button");
console.log(rbs);
for (var i=0;i<rbs.length;i++) {
    var rb = rbs[i];
    rb.addEventListener('click', function (e) {
    e.target.parentNode.remove();
    });
}