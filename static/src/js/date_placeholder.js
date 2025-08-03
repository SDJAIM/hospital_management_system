/** @odoo-module **/

import { registry } from "@web/core/registry";
import { DateField } from "@web/views/fields/date/date_field";

class DateFieldWithPlaceholder extends DateField {
    setup() {
        super.setup();
        // Set placeholder from XML field attribute if available
        this.placeholder = this.props.attrs?.placeholder || '';
    }

    _renderEdit() {
        const vnode = super._renderEdit();

        // Modify the input placeholder using patching the VNode (safe)
        if (vnode && vnode.tag === "input") {
            vnode.props = {
                ...vnode.props,
                placeholder: this.placeholder,
            };
        }

        return vnode;
    }
}

// Override default date field widget
registry.category("fields").add("date", DateFieldWithPlaceholder, { force: true });
