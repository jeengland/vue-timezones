<template>
    <div>
        <form @submit.prevent>
            <input type='number' name='hours' min='1' max='12' placeholder='HH' />
            <input type='number' name='minutes' min='0' max='59' placeholder="MM" />
        </form>
    </div>
</template>

<script>
    export default {
    }
</script>