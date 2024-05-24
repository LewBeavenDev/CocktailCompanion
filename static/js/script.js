$(function () {
  M.AutoInit();
});

function toggleModal() {
  let instance = M.Modal.getInstance($("#modal3"));
  instance.open();
}
