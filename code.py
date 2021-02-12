import markdown2
import structlog

log = structlog.get_logger()

### VIASH START
par = {
  'input': 'ipsum.md',
  'output': 'ipsum.html',
}
resource_dir = "."
### VIASH END

log.debug("Parameters", par=par)

log.debug("Read input ...", input=par['input'])
with open(par['input'], 'r') as f:
    text_md = f.read()

log.debug("Process input ...")
text_html = markdown2.markdown(text_md)

log.debug("Write output ...", input=par['output'])
with open(par['output'], 'w') as f:
    f.write(text_html)
