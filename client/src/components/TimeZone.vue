<template>
    <div>
        <form @submit.prevent='emitTime'>
            <input v-model='time.hour' type='number' name='hours' min='1' max='12' placeholder='hh' required/>
            <input v-model='time.minute' type='number' name='minutes' min='0' max='59' placeholder='mm' required/>
            <select v-model='time.isPM'>
                <option value='false'>AM</option>
                <option value='true'>PM</option>
            </select>
            <input v-model='time.date' type='date' name='date' required />
            <select v-model='time.from_TZ'>
                <option v-for="timezone in timezones" :key='timezone' :value='timezone'>{{timezone}}</option>
            </select>
            <select v-model='time.to_TZ'>
                <option v-for="timezone in timezones" :key='timezone' :value='timezone'>{{timezone}}</option>
            </select>
            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
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
                timezones: timezones
            }
        },
        methods: {
            emitTime() {
                console.log(this.time)
                this.$emit('time', this.time)
            }
        }
    }
</script>