const fs=require('fs'),vm=require('vm'),assert=require('assert');
const html=fs.readFileSync('lumos_user_guide.html','utf8');
const script=html.split('<script>')[1].split('</script>')[0];
const nodes={};
const node=id=>nodes[id]||(nodes[id]={style:{},classList:{add(){},remove(){}},getAttribute(name){return this[name]},clientHeight:720,textContent:'',innerHTML:''});
const context={document:{getElementById:node,querySelectorAll(){return[]},addEventListener(){}},requestAnimationFrame:fn=>fn()};
vm.createContext(context);vm.runInContext(script,context);
let checked=0;
for(const role of ['student','teacher']){
vm.runInContext(`chooseRole('${role}');cursor=0;render()`,context);
const count=vm.runInContext('journey.length',context);
for(let i=0;i<count;i++){
assert.equal((node('overlay').innerHTML.match(/class="bounding"/g)||[]).length,1);
assert(node('action').textContent.length>10);
assert(node('next').textContent.length>10);
const item=vm.runInContext('journey[cursor]',context);
assert(item.screen.role==='both'||item.screen.role===role);
const [x,y,w,h]=item.step.box,[iw,ih]=item.screen.size;
assert(x>=0&&y>=0&&w>0&&h>0&&x+w<=iw&&y+h<=ih);
assert.equal(node('back').disabled,i===0);assert.equal(node('forward').disabled,i===count-1);
vm.runInContext('move(1)',context);checked++;
}
assert.equal(vm.runInContext('cursor',context),count-1);
for(let i=count-1;i>0;i--)vm.runInContext('move(-1)',context);
assert.equal(vm.runInContext('cursor',context),0);
}
assert(!html.includes('hotspot-list'));
assert(html.indexOf('id="back"')>html.indexOf('id="image"'));
console.log('PASS:',checked,'steps; one box per step; role isolation; forward/back boundaries; pixel coordinates within image; arrows below image.');
