// @ts-check-js

import { lanyard } from 'https://github.com/xaronnn/js-lanyard/raw/fdee9366ade13ab9640b250982006a5541f60664/lanyard.js'


lanyard({
	userId: '153030101171175425',
	socket: true,
	onPresenceUpdate:
		(data) => {
			console.log('hello!', data);
		}
})

