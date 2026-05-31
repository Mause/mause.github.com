// @ts-check-js

import { connectWebSocket } from 'https://esm.sh/lanyard-wrapper@2.0.1'

connectWebSocket(
	'153030101171175425',
	(data) => {
		console.log('hello!', data);
		richStatus.textContent = `Status: ${data.discord_status}`
	}
)

const richStatus = document.getElementById('rich-status')
