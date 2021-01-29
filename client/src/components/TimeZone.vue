<template>
    <div class='card m-1 mx-auto mt-3 bg-dark text-light' style='width: 30rem'>
        <fieldset class='card-body' :disabled='disabled'>
            <h5 class='card-title text-center'>Convert Timezone</h5>
            <form @submit.prevent='emitTime'>
            <p class='mb-1'>Time:</p>
            <div class='form-group d-flex flex-row'>
                <label class='sr-only' for='hours'>Hours</label>
                <input class='form-control' v-model='time.hour' type='number' name='hours' id='hours' min='1' max='12' placeholder='hh' required/>
                <label class='sr-only' for='minutes'>Minutes</label>
                <input class='form-control' v-model='time.minute' type='number' name='minutes' id='minutes' min='0' max='59' placeholder='mm' required/>
                <label class='sr-only' for='amOrPm'>AM or PM</label>
                <select class='form-control' v-model='time.isPM' id='amOrPm'>
                    <option value='false'>AM</option>
                    <option value='true'>PM</option>
                </select>
            </div>
            <div class='form-group'>
                <label for='date' class='mb-1'>Date:</label>
                <input class='form-control' v-model='time.date' type='date' name='date' id='date' required />
            </div>
            <div class='form-group'>
                <label for='fromTz'>Timezone to convert from:</label>
                <select class='form-control' id='fromTz' v-model='time.from_TZ' required>
                    <option value="" disabled>Select timezone</option>
                    <option v-for="timezone in timezones" :key='timezone' :value='timezone'>{{timezone}}</option>
                </select>
            </div>
            <div class='form-group'>
                <label for='toTz'>Timezone to convert to:</label>
                <select class='form-control' id='toTz' v-model='time.to_TZ' required>
                    <option value="" disabled selected>Select timezone</option>
                    <option v-for="timezone in timezones" :key='timezone' :value='timezone'>{{timezone}}</option>
                </select>
            </div>
            <label class='sr-only' for='submit'>Submit</label>
            <button class='btn btn-secondary' id='submit' type="submit" :disabled='disabled'>Submit</button>
        </form>
        </fieldset>
    </div>
</template>

<script>
    // Timezones list sourced from IANA 
    import timezones from '../assets/timezones.json'
    const local_Tz = Intl.DateTimeFormat().resolvedOptions().timeZone
    const current = new Date()
    let month = (current.getMonth() + 1 ).toString().padStart(2, '0')
    let day = current.getDate().toString().padStart(2, '0')
    const curDate = `${current.getFullYear()}-${month}-${day}`
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
                    date: curDate,
                    hour: hr,
                    minute: current.getMinutes(), 
                    isPM: pm,
                    from_TZ: local_Tz,
                    to_TZ: ''
                },
                timezones: timezones,
                disabled: false,
            }
        },
        methods: {
            emitTime() {
                this.disabled = true
                this.$emit('time', this.time)
            }
        }
    }
</script>