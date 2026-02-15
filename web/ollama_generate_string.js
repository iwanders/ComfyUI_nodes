import { app } from "../../scripts/app.js";
import { api } from "../../scripts/api.js";
import { ComfyWidgets } from "../../scripts/widgets.js";

app.registerExtension({
  name: "iw.ollama.generate",

  async beforeRegisterNodeDef(nodeType, nodeData, app) { 
    let find_widget = (node, name) => node.widgets.find((w) => w.name === name);
    if (nodeData.name === "IW_OllamaGenerateString") {
      console.log("Something ollama thing");
      nodeType.prototype.initState = function () {
        console.log("hello");
      };
      nodeType.prototype.initWidgets = function (app) { 
        this.setupWidgets(); 
      };

      nodeType.prototype.setupWidgets = function (app) {
        this.addWidget(
          "combo",
          "model",
          "unknown",
          (value) => {
            this.tool = value;
          },
          {
            values: ["a", "b", "c"],
            default: "unknown",
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
 