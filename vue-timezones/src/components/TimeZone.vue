<template>
    <div>
        <form @submit.prevent='emitTime'>
            <input v-model='time.hour' type='number' name='hours' min='1' max='12' placeholder='HH' required/>
            <input v-model='time.minute' type='number' name='minutes' min='0' max='59' placeholder="MM" required/>
            <select v-model='time.aOrP'>
                <option value="AM">AM</option>
                <option value="PM">PM</option>
            </select>
            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                time: { 
                    hour: '',
                    minute: '', 
                    aOrP: 'AM' 
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