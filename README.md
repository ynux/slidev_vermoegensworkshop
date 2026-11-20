### Technical implementation

I decided to use Slidev and like it a lot. It is easy to write manually (md-Format) and for my AI buddy. I can show it at our workshop, publish it on a website and export it to other formats.

One issue i had to get used to was that the browser pointing to localhost will show errors after edits, something to do with the dynamic rendering, solved by restarting in the npwm run dev terminal. 

Install node, make sure that the binary is found, follow https://sli.dev/guide/#getting-started . On my Mac there were issues with the scripts in the pnpm installation, but creating the slidev base project still worked. 

To start the slide show:

- `npm install`
- `npm run dev`
- visit <http://localhost:3030>

Edit the [slides.md](./slides.md) to see the changes. 

I decided to split the file / import files into the main slides.md as https://sli.dev/features/importing-slides into a manual part and generated slides because Claude writes much more sophisticated markdown.

Learn more about Slidev at the [documentation](https://sli.dev/).
