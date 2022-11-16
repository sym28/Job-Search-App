const loader = document.querySelector('#loader')
loader.style.display = 'none'

const loadData = () => {
  loader.style.display = 'block'
}

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.parallax');
  var instances = M.Parallax.init(elems, options);
});