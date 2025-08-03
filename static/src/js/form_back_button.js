/** @odoo-module **/

import { registry } from '@web/core/registry';
import { FormController } from '@web/views/form/form_controller';

const customFormController = FormController.extend({
    setup() {
        super.setup();
        setTimeout(() => {
            const backBtn = this.el.querySelector('.btn-back');
            if (backBtn) {
                backBtn.addEventListener('click', () => {
                    this.onDiscard();  // Trigger native discard (no save)
                });
            }
        }, 0);
    }
});

registry.category('views').add('custom_form_with_back', {
    ...registry.category('views').get('form'),
    Controller: customFormController,
});
