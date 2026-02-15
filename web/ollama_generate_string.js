import { app } from "../../scripts/app.js";
import { api } from "../../scripts/api.js";
import { ComfyWidgets } from "../../scripts/widgets.js";


// This is helpful:
// https://github.com/Comfy-Org/ComfyUI_frontend/tree/0f0029ca29f4a11b37b84cd4d575280484bdd9e9/src/extensions/core

app.registerExtension({
  name: "iw.ollama.generate",

  async setup(app) {
    const resp = await api.fetchApi('/iw/api/ollama/models', { });

    if (resp.status !== 200) {
      const err = `Error uploading temp file: ${resp.status} - ${resp.statusText}`
      useToastStore().addAlert(err)
      throw new Error(err)
    }
    const result_in_json = await resp.json();
    const model_list = result_in_json.models; 

    app._iw_ollama_generate_string = {
      "model_list": model_list
    };

  },

  async beforeRegisterNodeDef(nodeType, nodeData, app) {
    let find_widget = (node, name) => node.widgets.find((w) => w.name === name); 
    let extension = this;

    if (nodeData.name === "IW_OllamaGenerateString") {


      console.log("Something ollama thing");

      nodeType.prototype.initState = function () {
        console.log("hello");
      };
      nodeType.prototype.initWidgets = function (app) {  
        this.setupWidgets(app._iw_ollama_generate_string.model_list);  
      };

      nodeType.prototype.setupWidgets = function (model_list) {
        // https://docs.comfy.org/custom-nodes/js/javascript_objects_and_hijacking#inputs-outputs-widgets
        //let default_model = model_list[0];
        //let w = find_widget(this, "model");
        //w.widgets_values = model_list; 
        //this.removeWidget("model");
        /*this.addWidget(
          "combo",
          "model",
          default_model,
          (value) => {
            this.tool = value;
          },
          {
            values: model_list,
            default: default_model,
          }
        );*/
 
      };


      nodeType.prototype.onNodeCreated = function () { 
        this.initWidgets(app);
        this.initState(); 
      };

      nodeType.prototype.onExecuted = function (ui) {
          // This is after the fact... so we ready the next value.
          console.log("onExecuted  ui:", ui);
          for (let orig_key of ["next_seed", "next_result", "next_prompt"]) {
            let next_key = orig_key.replace("next", "use"); 
            let w = find_widget(this, next_key);
            if (w !== undefined) {
              w.value = ui[orig_key][0];
              w.setValue(w.value, false, true); 
            }

          }

      }
    }
  }
});
 