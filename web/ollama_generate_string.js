import { app } from "../../scripts/app.js";
import { api } from "../../scripts/api.js";
import { ComfyWidgets } from "../../scripts/widgets.js";

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
        let default_model = model_list[0];

        this.addWidget(
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
        );
 
      };


      nodeType.prototype.onNodeCreated = function () { 
        this.initWidgets(app);
        this.initState(); 
      };

      nodeType.prototype.onExecuted = function (ui) {
          // This is after the fact... so we ready the next value.
          console.log("onExecuted  next_value", ui.next_value);
          let w = find_widget(this, "prompt");
          w.value = ui.next_value;
          w.setValue(w.value, false, true);

      }
    }
  }
});
 