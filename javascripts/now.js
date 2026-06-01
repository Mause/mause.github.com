// @ts-check-js

import { connectWebSocket } from 'https://esm.sh/lanyard-wrapper@2.0.1'

connectWebSocket(
	'153030101171175425',
	({discord_status, spotify}) => {
		richStatus.textContent = `Status: ${discord_status}`
		if (spotify) {
			richStatus.textContent += ` | Currenly listening to ${spotify.song}, by ${spotify.artist}`;
		}
	}
)

const richStatus = document.getElementById('rich-status')
