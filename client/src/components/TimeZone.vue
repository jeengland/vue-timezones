<template>
    <div>
        <form @submit.prevent='emitTime'>
            <input v-model='time.hour' type='number' name='hours' min='1' max='12' placeholder='HH' required/>
            <input v-model='time.minute' type='number' name='minutes' min='0' max='59' placeholder="MM" required/>
            <select v-model='time.isPM'>
                <option value='false'>AM</option>
                <option value='true'>PM</option>
            </select>
            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
    const current = new Date()
    let hr = current.getHours()
    let pm = false
    if (hr > 11) {
        pm = true
    }
    if (hr > 12) {
        hr -= 12
    }
    if (hr == 0) {
        hr = 12;
    }

    export default {
        data() {
            return {
                time: { 
                    hour: hr,
                    minute: current.getMinutes(), 
                    isPM: pm
                }
            }
        },
        methods: {
            emitTime() {
                this.$emit('time', this.time)
            }
        }
    }
</script>