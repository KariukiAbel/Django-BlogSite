const titleImput = document.querySelector('input[name=title]');
const slugImput = document.querySelector('input[name=slug]');


const slugify = (val) => {
  return val.toString().toLowerCase().trim()
  .replace(/&/g,"-and-")  //replace & with '-and-'
  .replace(/[\s\W-]+/g, '-') //replaces spaces, non word chars and dashes with a single dashes

};

titleImput.addEventListener('keyup', (e)=>{
slugImput.setAttribute('value', slugify(titleImput.value));
});
