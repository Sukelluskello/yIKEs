#!/usr/bin/python3
#information was copied from https://raw.githubusercontent.com/royhills/ike-scan/master/ike-vendor-ids 
# thanks to The IKE Scanner (ike-scan) and Roy Hills

vendor_IDs = {
	"^1e2b516905991c7d7c96fcbfb587e46100000002":"Windows-2000",
	"^1e2b516905991c7d7c96fcbfb587e46100000003":"Windows-XP-SP1",
	"^1e2b516905991c7d7c96fcbfb587e46100000004":"Windows-2003-or-XP-SP2",
	"^1e2b516905991c7d7c96fcbfb587e46100000005":"Windows-Vista",
	"^1e2b516905991c7d7c96fcbfb587e46100000006":"Windows-2008",
	"^1e2b516905991c7d7c96fcbfb587e46100000007":"Windows-7",
	"^1e2b516905991c7d7c96fcbfb587e46100000008":"Windows-2008-R2",
	"^1e2b516905991c7d7c96fcbfb587e46100000009":"Windows-8",
	"^1e2b516905991c7d7c96fcbfb587e46100000010":"Windows-2012",
	"^1e2b516905991c7d7c96fcbfb587e46.........":"Windows",
	"^f4ed19e0c114eb516faaac0ee37daf2807b4381f00000001000000020000000000000000........":"Firewall-1 4.1 Base",
	"^f4ed19e0c114eb516faaac0ee37daf2807b4381f00000001000000030000000000000000........":"Firewall-1 4.1 SP1",
	"^f4ed19e0c114eb516faaac0ee37daf2807b4381f0000000100000fa20000000000000000........":"Firewall-1 4.1 SP2-SP6",
	"^f4ed19e0c114eb516faaac0ee37daf2807b4381f00000001000013880000000000000000........":"Firewall-1 NG Base",
	"^f4ed19e0c114eb516faaac0ee37daf2807b4381f00000001000013890000000000000000........":"Firewall-1 NG FP1",
	"^f4ed19e0c114eb516faaac0ee37daf2807b4381f000000010000138a0000000000000000........":"Firewall-1 NG FP2",
	"^f4ed19e0c114eb516faaac0ee37daf2807b4381f000000010000138b0000000000000000........":"Firewall-1 NG FP3",
	"^f4ed19e0c114eb516faaac0ee37daf2807b4381f000000010000138c0000000000000000........":"Firewall-1 NG AI R54",
	"^f4ed19e0c114eb516faaac0ee37daf2807b4381f000000010000138d0000000000000000........":"Firewall-1 NG AI R55",
	"^f4ed19e0c114eb516faaac0ee37daf2807b4381f000000010000138d........00000000........":"Firewall-1 NGX or later",
	"^f4ed19e0c114eb516faaac0ee37daf2807b4381f":"Firewall-1 Unknown Vsn",
	"^afcad71368a1f1c96b8696fc77570100":"Dead Peer Detection v1.0",
	"^afcad71368a1f1c96b8696fc7757....":"Dead Peer Detection",
	"^09002689dfd6b712":"XAUTH",
	"^fbf47614984031fa8e3bb6198089b223":"SSH IPSEC Express 1.1.0",
	"^1952dc91ac20f646fb01cf42a33aee30":"SSH IPSEC Express 1.1.1",
	"^e8bffa643e5c8f2cd10fda7370b6ebe5":"SSH IPSEC Express 1.1.2",
	"^c1111b2dee8cbc3d620573ec57aab9cb":"SSH IPSEC Express 1.2.1",
	"^09ec27bfbc09c75823cfecbffe565a2e":"SSH IPSEC Express 1.2.2",
	"^7f21a596e4e318f0b2f4944c2384cb84":"SSH IPSEC Express 2.0.0",
	"^2836d1fd2807bc9e5ae30786320451ec":"SSH IPSEC Express 2.1.0",
	"^a68de756a9c5229bae66498040951ad5":"SSH IPSEC Express 2.1.1",
	"^3f2372867e237c1cd8250a75559cae20":"SSH IPSEC Express 2.1.2",
	"^0e58d5774df602007d0b02443660f7eb":"SSH IPSEC Express 3.0.0",
	"^f5ce31ebc210f44350cf71265b57380f":"SSH IPSEC Express 3.0.1",
	"^f64260af2e2742daddd56987068a99a0":"SSH IPSEC Express 4.0.0",
	"^7a54d3bdb3b1e6d923892064be2d981c":"SSH IPSEC Express 4.0.1",
	"^9aa1f3b43472a45d5f506aeb260cf214":"SSH IPSEC Express 4.1.0",
	"^89f7b760d86b012acf263382394d962f":"SSH IPSEC Express 4.1.1",
	"^6880c7d026099114e486c55430e7abee":"SSH IPSEC Express 4.2.0",
	"^b037a21aceccb5570f602546f97bde8c":"SSH IPSEC Express 5.0",
	"^2b2dad97c4d140930053287f996850b0":"SSH IPSEC Express 5.0.0",
	"^45e17f3abe93944cb202910c59ef806b":"SSH IPSEC Express 5.1.0",
	"^5925859f7377ed7816d2fb81c01fa551":"SSH IPSEC Express 5.1.1",
	"^12f5f28c457168a9702d9fe274cc0100":"Cisco Unity",
	"^1f07f70eaa6514d3b0fa96542a500300":"Cisco VPN Concentrator (3.0.0)",
	"^1f07f70eaa6514d3b0fa96542a500301":"Cisco VPN Concentrator (3.0.1)",
	"^1f07f70eaa6514d3b0fa96542a500305":"Cisco VPN Concentrator (3.0.5)",
	"^1f07f70eaa6514d3b0fa96542a500407":"Cisco VPN Concentrator (4.0.7)",
	"^f6f7efc7f5aeb8cb158cb9d094ba69e7":"VPN-3000-client",
	"^1f07f70eaa6514d3b0fa96542a":"Cisco VPN Concentrator",
	"^4048b7d56ebce88525e7de7f00d6c2d3":"IKE Fragmentation",
	"^27bab5dc01ea0760ea4e3190ac27c0d0":"draft-stenberg-ipsec-nat-traversal-01",
	"^6105c422e76847e43f9684801292aecd":"draft-stenberg-ipsec-nat-traversal-02",
	"^6a7434c19d7e36348090a02334c9c805":"draft-huttunen-ipsec-esp-in-udp-00.txt",
	"^47bbe7c993f1fc13b4e6d0db565c68e5010201010201010310382e302e3020284275696c6420313029000000":"SafeNet SoftRemote 8.0.0",
	"^47bbe7c993f1fc13b4e6d0db565c68e5010201010201010310392e302e3120284275696c6420313229000000":"SafeNet SoftRemote 9.0.1",
	"^47bbe7c993f1fc13b4e6d0db565c68e5":"SafeNet SoftRemote",
	"^4865617274426561745f4e6f74696679":"HeartBeat_Notify",
	"^486561727442656174204e6f74696679":"HeartBeat Notify",
	"^4f70656e5047503130313731":"OpenPGP",
	"^50760f624c63e5c53eea386c685ca083":"ESPThruNAT",
	"^054182a07c7ae206f9d2cf9d2432c482":"SSH Sentinel",
	"^b91623e693ca18a54c6a2778552305e8":"SSH Sentinel 1.1",
	"^5430888de01a31a6fa8f60224e449958":"SSH Sentinel 1.2",
	"^7ee5cb85f71ce259c94a5c731ee4e752":"SSH Sentinel 1.3",
	"^63d9a1a7009491b5a0a6fdeb2a8284f0":"SSH Sentinel 1.4",
	"^eb4b0d96276b4e220ad16221a7b2a5e6":"SSH Sentinel 1.4.1",
	"^54494d4553544550":"Timestep",
	"^7003cbc1097dbe9c2600ba6983bc8b35":"KAME/racoon",
	"^4df37928e9fc4fd1b3262170d515c662":"draft-ietf-ipsec-nat-t-ike",
	"^4485152d18b6bbcd0be8a8469579ddcc":"draft-ietf-ipsec-nat-t-ike-00",
	"^16f6ca16e4a4066d83821a0f0aeaa862":"draft-ietf-ipsec-nat-t-ike-01",
	"^90cb80913ebb696e086381b5ec427b1f":"draft-ietf-ipsec-nat-t-ike-02\n",
	"^cd60464335df21f87cfdb2fc68b6a448":"draft-ietf-ipsec-nat-t-ike-02",
	"^7d9419a65310ca6f2c179d9215529d56":"draft-ietf-ipsec-nat-t-ike-03",
	"^9909b64eed937c6573de52ace952fa6b":"draft-ietf-ipsec-nat-t-ike-04",
	"^80d0bb3def54565ee84645d4c85ce3ee":"draft-ietf-ipsec-nat-t-ike-05",
	"^4d1e0e136deafa34c4f3ea9f02ec7285":"draft-ietf-ipsec-nat-t-ike-06",
	"^439b59f8ba676c4c7737ae22eab8f582":"draft-ietf-ipsec-nat-t-ike-07",
	"^8f8d83826d246b6fc7a8a6a428c11de8":"draft-ietf-ipsec-nat-t-ike-08",
	"^42ea5b6f898d9773a575df26e7dd19e1":"draft-ietf-ipsec-nat-t-ike-09",
	"^c40fee00d5d39ddb1fc762e09b7cfea7":"Testing NAT-T RFC",
	"^810fa565f8ab14369105d706fbd57279":"RFC XXXX",
	"^4a131c81070358455c5728f20e95452f":"RFC 3947 NAT-T",
	"^1e2b516905991c7d7c96fcbfb587e461":"MS NT5 ISAKMPOAKLEY",
	"^ad2c0dd0b9c32083ccba25b8861ec455":"A GSS-API Authentication Method for IKE",
	"^b46d8914f3aaa3f2fedeb7c7db2943ca":"A GSS-API Authentication Method for IKE\n",
	"^621b04bb09882ac1e15935fefa24aeee":"GSSAPI",
	"^72872B95FCDA2EB708EFE322119B4971":"NLBS_PRESENT",
	"^214ca4faffa7f32d6748e5303395ae83":"MS-MamieExists",
	"^fb1de3cdf341b7ea16b7e5be0855f120":"MS-Negotiation Discovery Capable",
	"^e3a5966a76379fe707228231e5ce8652":"IKE CGA version 1",
	"^424e4553000000..":"Nortel Contivity",
	"^5b362bc820f60001":"SonicWall-1",
	"^5b362bc820f60002":"SonicWall-2",
	"^5b362bc820f60003":"SonicWall-3",
	"^5b362bc820f60005":"SonicWall-5",
	"^5b362bc820f60006":"SonicWall-6",
	"^5b362bc820f60007":"SonicWall-7",
	"^5b362bc820f60008":"SonicWall-8",
	"^404bf439522ca3f6":"SonicWall-a",
	"^da8e937880010000":"SonicWall-b",
	"^5b362bc820f70001":"SonicWall-c",
	"^37eba0c4136184e7daf8562a77060b4a":"SSH QuickSec 0.9.0",
	"^5d72925e55948a9661a7fc48fdec7ff9":"SSH QuickSec 1.1.0",
	"^777fbf4c5af6d1cdd4b895a05bf82594":"SSH QuickSec 1.1.1",
	"^2cdf08e712ede8a5978761267cd19b91":"SSH QuickSec 1.1.2",
	"^59e454a8c2cf02a34959121f1890bc87":"SSH QuickSec 1.1.3",
	"^8f9cc94e01248ecdf147594c284b213b":"SSH QuickSec 2.1.0",
	"^dbfb81eb5760b0788562067da102d755":"Netgear",
	"^ba290499c24e84e53a1d83a05e5f00c9":"IKE Challenge-Response",
	"^0d33611a5d521b5e3c9c03d2fc107e12":"IKE Challenge-Response-2",
	"^ad3251042cdc4652c9e0734ce5de4c7d":"IKE Challenge-Response Revised",
	"^13f11823f966fa91900f024ba66a86ba":"IKE Challenge-Response Revised-2",
	"^325df29a2319f2dd":"draft-krywaniuk-ipsec-antireplay-00",
	"^8db7a41811221660":"draft-ietf-ipsec-heartbeats-00",
	"^4d6163204f53582031302e78":"MacOS 10.x-1",
	"^4df37928e9fc4fd1b3262170d515c662":"MacOS 10.x-2",
	"^882fe56d6fd20dbc2251613b2ebe5beb":"strongSwan",
	"^9e10a0d4205edc6c90bd5381a53c2d2b":"strongSwan 5.1.1",
	"^a55a90de781611f70cbbae7045a225fc":"strongSwan 5.1.1rc1",
	"^c90b020d043f1f050ba809e13dc8234e":"strongSwan 5.1.1dr4",
	"^06f2f1b82256dce62c07cb4f71604035":"strongSwan 5.1.1dr3",
	"^4f130d312ec92f50c02f2b0eb60d6ccc":"strongSwan 5.1.1dr2",
	"^1a45d3bda55646016e998ac1c5590e59":"strongSwan 5.1.1dr1",
	"^b7d8e62184049fb21b088d4232d2549c":"strongSwan 5.1.0",
	"^02c49867060173c665ebce2b8110c7f7":"strongSwan 5.1.0rc1",
	"^e069a583c5640257a8de2cf062461a4b":"strongSwan 5.1.0dr2",
	"^22982eab040be7a4cb4177da312f2f1c":"strongSwan 5.1.0dr1",
	"^dc3afcdda0514da394b4b36f4cb1b9a7":"strongSwan 5.0.4",
	"^d398476a43b9d6c56c4045ffcc9fffb9":"strongSwan 5.0.3",
	"^f2d4de999721c37fea51d4bcbc060120":"strongSwan 5.0.3rc1",
	"^f4d68a2fb63e4390a959baa5c4bc7598":"strongSwan 5.0.3dr3",
	"^7b3f3d21e4768e010fc7dd04ae369c61":"strongSwan 5.0.3dr2",
	"^ca7d77d20794391df5a3cb90fbf5b72e":"strongSwan 5.0.3dr1",
	"^04d52cc5fd04aa971063b111917731d2":"strongSwan 5.0.2",
	"^80b8f4380b18f24f03ce5745fc3db56b":"strongSwan 5.0.2rc1",
	"^a5f8ce0d6751c640e55bc41784f2e081":"strongSwan 5.0.2dr4",
	"^75aa8f69de2e44500dae842be21f5491":"strongSwan 5.0.1",
	"^e154b11a96ee2b44d4954843cd3a40a3":"strongSwan 5.0.0",
	"^a87680d00cbb939871eb680d18d052e2":"strongSwan 4.6.4",
	"^984a7bfefb46489a5be74b64531c6753":"strongSwan 4.6.3",
	"^9c73b19f5f4181aa4b269dd004608811":"strongSwan 4.6.2",
	"^1d6cfa4d69d9d33c0b2244bf99de9b8b":"strongSwan 4.6.1",
	"^41ef2e2f7ec8b923c98d9fa9bb7a04a5":"strongSwan 4.6.0",
	"^75244ad8a5a0f48e7e3b7ad79dcab153":"strongSwan 4.5.3",
	"^b149d6161fb4c7c3805beeff042d08c0":"strongSwan 4.5.2",
	"^efe12e8533bbcf4e978ec874935e9972":"strongSwan 4.5.1",
	"^eff89e6f406f55292807c3b8f925884a":"strongSwan 4.5.0",
	"^aaa2e272c58de8f96e72c4c21ba7dd99":"strongSwan 4.4.1",
	"^a5ad81e15e1c68a1be277abfeee80d94":"strongSwan 4.4.0",
	"^02d7c3a0698ec33bb126b2baa70b9c2c":"strongSwan 4.3.7",
	"^882fe56d6fd20dbc2251613b2ebe5beb":"strongSwan 4.3.6",
	"^117c406d20a29f56f0dfcb03d9fa835b":"strongSwan 4.3.5rc1",
	"^de5c703801952d85f6b3ed33b33784b4":"strongSwan 4.3.5",
	"^e37e5d64a329a5cf1eeb8546c3b06018":"strongSwan 4.3.4",
	"^f9f093629308b24388d09c3f026de0a8":"strongSwan 4.3.3",
	"^d6263956ac790961a9c8409b393724bf":"strongSwan 4.3.2",
	"^20b1f62b240a52a849309183960cbb64":"strongSwan 4.3.1",
	"^9deb74e751f44c47905ed2fad93f9271":"strongSwan 4.3.0",
	"^488c08f57afc382112f7cb396f2d4f6c":"strongSwan 4.2.9",
	"^95569ee23ebb62eddedea353a575faf3":"strongSwan 4.2.8",
	"^4ddc7e1f6d6cd1ae9d5dcac58fa1fe9a":"strongSwan 4.2.7",
	"^a2782dd683b5edee3b777f897d2b867e":"strongSwan 4.2.6",
	"^af0a05e0bd37b0aba0135a194abb5b89":"strongSwan 4.2.5",
	"^cd5792d4b70f0299a6a1373de236d2ac":"strongSwan 4.2.4",
	"^2d1f406118fbd5d28474791ffa00488a":"strongSwan 4.2.3",
	"^2a517d0d23c37d08bce7c292a0217b39":"strongSwan 4.2.2",
	"^bab253f4cb10a8108a7c927c56c87886":"strongSwan 4.2.1",
	"^9f68901325a972894335302a9531ab9f":"strongSwan 4.2.0",
	"^b7bd9f2f978e3259a7aa9f7a1396ad6c":"strongSwan 4.1.11",
	"^bf3a89ae5bef8e72d44dac8bb88d7d5f":"strongSwan 4.1.10",
	"^78fdd287def01a3f074b5369eab4fd1c":"strongSwan 4.1.9",
	"^66a2045507c119da78a4666259cdea48":"strongSwan 4.1.8",
	"^ea840aa4dfc9712d6c32b5a16eb329a3":"strongSwan 4.1.7",
	"^d19683368af4b0edc21ccde982b1d1b0":"strongSwan 4.1.6",
	"^bf0fbf7306ebb7827042d893539886e2":"strongSwan 4.1.5",
	"^312f9cb1a6b90e19de7528c904ac3087":"strongSwan 4.1.4",
	"^5849ab6d8beabd6e4d09e5a3b88c089a":"strongSwan 4.1.3",
	"^15a1ace7ee52fddfef04f928db2dd134":"strongSwan 4.1.2",
	"^d3f1c488c368175d5f40a8f5ca5f5e12":"strongSwan 4.1.1",
	"^4794cef6843422980d1a3d06af41c5cd":"strongSwan 4.1.0",
	"^ab0746221cc8fd0d5238f73a9b3da557":"strongSwan 4.0.7",
	"^4c90136946577b51919d8d9a6b8e4a9f":"strongSwan 4.0.6",
	"^dd180d21e5ce655a768ba32211dd8ad9":"strongSwan 4.0.5",
	"^1ef283f83549b5ff9608b6d634f84d75":"strongSwan 4.0.4",
	"^b181b18e114fc209b3c6e26c3a80718e":"strongSwan 4.0.3",
	"^77e8eea6f556a499de3ffe7f7f95661c":"strongSwan 4.0.2",
	"^9dbbafcf1db0dd595ae065294003ad3e":"strongSwan 4.0.1",
	"^2ce9c946a4c879bf11b50b76cc5692cb":"strongSwan 4.0.0",
	"^0e9e820524932da199a498953afa8a7e":"strongSwan 2.8.9",
	"^8c4a3bcb729b11f703d22a5b39640ca8":"strongSwan 2.8.8",
	"^3a0d4e7ca4e492ed4dfe476d1ac6018b":"strongSwan 2.8.7",
	"^fe3f49706e26a9fb36a87bfce9ea36ce":"strongSwan 2.8.6",
	"^4c7efa31b39e510432a317570d97bbb9":"strongSwan 2.8.5",
	"^76c72bfd398424dd001b86d0012fe061":"strongSwan 2.8.4",
	"^fb4641ad0eeb2a34491d15f4eff51063":"strongSwan 2.8.3",
	"^299932277b7dfe382ce23465333a7d23":"strongSwan 2.8.2",
	"^e37f2d5ba89a62cd202ee27dac06c8a8":"strongSwan 2.8.1",
	"^32f0e9b9c06dfe8c9ad5599a636971a1":"strongSwan 2.8.0",
	"^7f50cc4ebf04c2d9da73abfd69b77aa2":"strongSwan 2.7.3",
	"^a194e2aaddd0bafb95253dd96dc733eb":"strongSwan 2.7.2",
	"^8134878582121785ba65ea345d6ba724":"strongSwan 2.7.1",
	"^07fa128e4754f9447b1dd46374eef360":"strongSwan 2.7.0",
	"^b927f95219a0fe3600dba3c1182ae55f":"strongSwan 2.6.4",
	"^b2860e7837f711bef3d0eeb106872ded":"strongSwan 2.6.3",
	"^5b1cd6fe7d050eda6c93871c107db3d2":"strongSwan 2.6.2",
	"^66afbc12bbfe6ce108b1f69f4bc917b7":"strongSwan 2.6.1",
	"^3f3266499ffdbd85950e702298062844":"strongSwan 2.6.0",
	"^1f4442296b83d7e33a8b45209ba0e590":"strongSwan 2.5.7",
	"^3c5eba3d8564928e32ae43c3d9924dee":"strongSwan 2.5.6",
	"^3f267ed621ada7ee6c7d8893ccb0b14b":"strongSwan 2.5.5",
	"^7a6bf5b7df89642a75a78ef7d657c1c0":"strongSwan 2.5.4",
	"^df5b1f0f1d5679d9f8512b16c55a6065":"strongSwan 2.5.3",
	"^861ce5eb72164b190e9e629a31cf4901":"strongSwan 2.5.2",
	"^9a4a4648f60f8eda7cfcbfe271ee5b7d":"strongSwan 2.5.1",
	"^9eb3d907ed7ada4e3cbcacb917abc8e4":"strongSwan 2.5.0",
	"^485a70361b4433b31dea1c6be0df243e":"strongSwan 2.4.4",
	"^982b7a063a33c143a8eadc88249f6bcc":"strongSwan 2.4.3",
	"^e7a3fd0c6d771a8f1b8a86a4169c9ea4":"strongSwan 2.4.2",
	"^75b0653cb281eb26d31ede38c8e1e228":"strongSwan 2.4.1",
	"^e829c88149bab3c0cee85da60e18ae9b":"strongSwan 2.4.0",
	"^42a4834c92ab9a7777063afa254bcb69":"strongSwan 2.3.2",
	"^f697c1afcc2ec8ddcdf99dc7af03a67f":"strongSwan 2.3.1",
	"^b8f92b2fa2d3fe5fe158344bda1cc6ae":"strongSwan 2.3.0",
	"^99dc7cc823376b3b33d04357896ae07b":"strongSwan 2.2.2",
	"^d9118b1e9de5efced9cc9d883f2168ff":"strongSwan 2.2.1",
	"^85b6cbec480d5c8cd9882c825ac2c244":"strongSwan 2.2.0",
	"^b858d1addd08c1e8adafea150608aa4497aa6cc8":"ZyXEL ZyWALL Router",
	"^f758f22668750f03b08df6ebe1d0":"ZyXEL ZyWALL USG 100",
	"^625027749d5ab97f5616c1602765cf480a3b7d0b":"ZyXEL ZyWALL",
	"^26244d38eddb61b3172a36e3d0cfb819":"Microsoft Initial-Contact",
	"^4f454a734e486b4a4c656272":"Linux FreeS/WAN 0.5",
	"^4f456c4f6b6251695c7c4674":"Linux FreeS/WAN 0.6",
	"^4f4548604f7f426647775453":"Linux FreeS/WAN 0.7",
	"^4f456462595d67595351445c":"Linux FreeS/WAN 0.7.1",
	"^4f457c625363787f517e6544":"Linux FreeS/WAN 0.7.2",
	"^4f4569517b587444694c4367":"Linux FreeS/WAN 0.8",
	"^4f45776a7f6d5e7a415d6f7c":"Linux FreeS/WAN 0.8.1",
	"^4f454f575c595a744a7d4f78":"Linux FreeS/WAN 0.8.2",
	"^4f45676a5553715e794f4f48":"Linux FreeS/WAN 0.8.3",
	"^4f45664250754b79577f5d55":"Linux FreeS/WAN 0.8.4",
	"^4f45615f4d44507343785d7b":"Linux FreeS/WAN 0.8.5",
	"^4f45494f5e4f746c57664157":"Linux FreeS/WAN 0.9",
	"^4f45494654445c41425d6d7b":"Linux FreeS/WAN 0.9.1",
	"^4f45497d4f7e6e5d60525170":"Linux FreeS/WAN 0.9.10",
	"^4f454b486274755358555140":"Linux FreeS/WAN 0.9.11",
	"^4f45694146645c4d4362727b":"Linux FreeS/WAN 0.9.12",
	"^4f45556c7d7671444b474c59":"Linux FreeS/WAN 0.9.13",
	"^4f456640625376587d626277":"Linux FreeS/WAN 0.9.14",
	"^4f454b796672767d437d5d5a":"Linux FreeS/WAN 0.9.15",
	"^4f454f62767d78797d7f6579":"Linux FreeS/WAN 0.9.16",
	"^4f45565b597d556e596e5e60":"Linux FreeS/WAN 0.9.17",
	"^4f45637e47544c77644a5b76":"Linux FreeS/WAN 0.9.18",
	"^4f45614d4873425c42727b63":"Linux FreeS/WAN 0.9.19",
	"^4f456171784e6b594a497058":"Linux FreeS/WAN 0.9.2",
	"^4f455c6d6c497f764f44477b":"Linux FreeS/WAN 0.9.20",
	"^4f4560624076527767787c56":"Linux FreeS/WAN 0.9.21",
	"^4f4541687e4c507a405d5146":"Linux FreeS/WAN 0.9.22",
	"^4f457841597142737f44787d":"Linux FreeS/WAN 0.9.23",
	"^4f457145706b5560634e725f":"Linux FreeS/WAN 0.9.24",
	"^4f454e5b60465a5a53656967":"Linux FreeS/WAN 0.9.25",
	"^4f45677c575b4c7c6a4a7173":"Linux FreeS/WAN 0.9.26",
	"^4f455f7f606c66424e616a60":"Linux FreeS/WAN 0.9.27",
	"^4f454e6d545e534c4a626063":"Linux FreeS/WAN 0.9.28",
	"^4f45765a4a6a51584653424e":"Linux FreeS/WAN 0.9.29",
	"^4f45485e6175794375444950":"Linux FreeS/WAN 0.9.3",
	"^4f45684e6772456542755d69":"Linux FreeS/WAN 0.9.30",
	"^4f45764141405f577750567b":"Linux FreeS/WAN 0.9.31",
	"^4f45546d5d704f49785e6467":"Linux FreeS/WAN 0.9.32",
	"^4f45655d786b445b75484668":"Linux FreeS/WAN 0.9.33",
	"^4f456547696d46657a4e5371":"Linux FreeS/WAN 0.9.34",
	"^4f455b76646a646f79695451":"Linux FreeS/WAN 0.9.35",
	"^4f454d596b6a6e5f56707e49":"Linux FreeS/WAN 0.9.36",
	"^4f45757b6e79665a556c6546":"Linux FreeS/WAN 0.9.37",
	"^4f455b6b636e606f5b42707b":"Linux FreeS/WAN 0.9.38",
	"^4f45677e79657a56654f7145":"Linux FreeS/WAN 0.9.39",
	"^4f4551604748445356727b74":"Linux FreeS/WAN 0.9.4",
	"^4f456e504e735f4f67555d5f":"Linux FreeS/WAN 0.9.40",
	"^4f4549557964647c42614440":"Linux FreeS/WAN 0.9.5",
	"^4f4570695578777266796a56":"Linux FreeS/WAN 0.9.6",
	"^4f457b4a767a6f716e48566c":"Linux FreeS/WAN 0.9.7",
	"^4f455b71457d4f685c475d6c":"Linux FreeS/WAN 0.9.8",
	"^4f455e4f4d58404f604d595c":"Linux FreeS/WAN 0.9.9",
	"^4f457f685e7d4c5645785669":"Linux FreeS/WAN 1.0.0",
	"^4f457176515f515f71526b56":"Linux FreeS/WAN 1.0.1",
	"^4f45465d56636a5149725558":"Linux FreeS/WAN 1.0.2",
	"^4f454644595a4f5c7a535445":"Linux FreeS/WAN 1.1.0",
	"^4f456842537e5a5c71527547":"Linux FreeS/WAN 1.1.1",
	"^4f457d5b4a707d736e7b5b6f":"Linux FreeS/WAN 1.1.2",
	"^4f45646357714a755b4a5b72":"Linux FreeS/WAN 1.1.3",
	"^4f454160444e745150604e47":"Linux FreeS/WAN 1.1.4",
	"^4f4544547476647754795157":"Linux FreeS/WAN 1.1.5",
	"^4f454b48657b616b494a4c77":"Linux FreeS/WAN 1.1.6",
	"^4f45544e79737d4953437b43":"Linux FreeS/WAN 1.2.0",
	"^4f454d524173695157515375":"Linux FreeS/WAN 1.2.1",
	"^4f45465e5c62774e59774c4f":"Linux FreeS/WAN 1.2.2",
	"^4f455a717b40607977577067":"Linux FreeS/WAN 1.3.0",
	"^4f457d7c696569676a6f607c":"Linux FreeS/WAN 1.3.1",
	"^4f457c6f70766b5a61546a51":"Linux FreeS/WAN 1.3.2",
	"^4f457d5b527b6c54736d447d":"Linux FreeS/WAN 1.3.3",
	"^4f454e746f4f53427579497d":"Linux FreeS/WAN 1.3.4",
	"^4f45415262734d596d56516b":"Linux FreeS/WAN 1.3.5",
	"^4f456248514f405942447c4e":"Linux FreeS/WAN 1.3.6",
	"^4f45404063756a5d496a584f":"Linux FreeS/WAN 1.4.0",
	"^4f455f526760425742497c65":"Linux FreeS/WAN 1.4.1",
	"^4f456270434d5b6e6753776e":"Linux FreeS/WAN 1.4.2",
	"^4f457a6d5b605b7d42405a67":"Linux FreeS/WAN 1.4.3",
	"^4f457177674d6a63426e4d54":"Linux FreeS/WAN 1.4.4",
	"^4f457d73435c6d5b6e777d59":"Linux FreeS/WAN 1.4.5",
	"^4f45425261435763654e5269":"Linux FreeS/WAN 1.4.6",
	"^4f457a6a547b434378757857":"Linux FreeS/WAN 1.4.7",
	"^4f455476696c4e50675f6e70":"Linux FreeS/WAN 1.4.8",
	"^4f455676404f5b55457d5479":"Linux FreeS/WAN 1.5.0",
	"^4f45617072517b7d5c607344":"Linux FreeS/WAN 1.5.1",
	"^4f456f407272744071414846":"Linux FreeS/WAN 1.5.2",
	"^4f4547425f74447179614445":"Linux FreeS/WAN 1.5.3",
	"^4f457d667c7069487e495448":"Linux FreeS/WAN 1.5.4",
	"^4f45505f70774e73435e5b7a":"Linux FreeS/WAN 1.5.5",
	"^4f45467c4d4760617f486547":"Linux FreeS/WAN 1.6.0",
	"^4f454b534c5842715a656f49":"Linux FreeS/WAN 1.6.1",
	"^4f4557464c67535540427a72":"Linux FreeS/WAN 1.6.2",
	"^4f457d60727152596653686e":"Linux FreeS/WAN 1.6.3",
	"^4f45486b7d44784d42676b5d":"Linux FreeS/WAN 2.00",
	"^4f457c4f547e6e615b426e56":"Linux FreeS/WAN 2.01",
	"^4f456c6b44696d7f6b4c4e60":"Linux FreeS/WAN 2.02",
	"^4f45566671474962734e6264":"Linux FreeS/WAN 2.03",
	"^4f45704f736579505c6e5f6d":"Linux FreeS/WAN 2.04",
	"^4f457271785f4c7e496f4d54":"Linux FreeS/WAN 2.05",
	"^4f457e4c466e5d427c5c6b52":"Linux FreeS/WAN 2.06",
	"^4f455d787a5b6948787a655b":"Openswan 2.1.0",
	"^4f45466a786e57484d4d4361":"Openswan 2.1.1",
	"^4f4555656771407e63636578":"Openswan 2.1.2",
	"^4f4548724b6e5e68557c604f":"Openswan 2.2.0",
	"^4f4572696f5c77557f746249":"Openswan 2.3.0",
	"^4f45454355706e735d625c71":"Openswan 2.3.1",
	"^4f45436f586c544d46766f54":"Openswan 2.3.1 X.509-1.5.4 LDAP_V3 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f454578616c467b5f6f606d":"Openswan 2.3.1 X.509-1.5.4 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f45785c567c6f61507e7864":"Openswan 2.4.0",
	"^4f457240604e7f585d6d5869":"Openswan 2.4.0 X.509-1.5.4 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f456e5e4c737d7d62796c51":"Openswan 2.4.1",
	"^4f456971726d54726e464a71":"Openswan 2.4.10",
	"^4f4574715e655577567a5f41":"Openswan 2.4.10 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f4550484948576e64636f6b":"Openswan 2.4.11",
	"^4f457b64445e664a6355766b":"Openswan 2.4.11 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f456c7c5b79725e4a6a5658":"Openswan 2.4.12",
	"^4f45606c50487c5662707575":"Openswan 2.4.12 LDAP_V3 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f454b427a64597b774d5d40":"Openswan 2.4.12 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f45445e597f60634770436c":"Openswan 2.4.13",
	"^4f456b5a5d52605d7a7a6f4e":"Openswan 2.4.13 LDAP_V3 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f456066696a417566514d44":"Openswan 2.4.13 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f454c4e767d475b775e6f56":"Openswan 2.4.14",
	"^4f455a526b5f4c686e534e63":"Openswan 2.4.14 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f45675d5e5d7f664c604651":"Openswan 2.4.15",
	"^4f4540784e47627163627858":"Openswan 2.4.15 LDAP_V3 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f457d78546050757b707245":"Openswan 2.4.15 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f45666a6343554b5f7a4062":"Openswan 2.4.2",
	"^4f4547407c7673775449546e":"Openswan 2.4.3",
	"^4f455b7075417d5959587e46":"Openswan 2.4.3 X.509-1.5.4 LDAP_V3 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f45565e6441545f4a664642":"Openswan 2.4.4",
	"^4f457a7d4646466667725f65":"Openswan 2.4.4 X.509-1.5.4 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f45587d5d4b4b7c61487b7c":"Openswan 2.4.5",
	"^4f454766754a5b59657b4168":"Openswan 2.4.5 X.509-1.5.4 LDAP_V3 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f456e4d43757f784f704063":"Openswan 2.4.5 X.509-1.5.4 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f45725c5b754061666c425f":"Openswan 2.4.5dr3 X.509-1.5.4 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f45636e6542785f6f6b7257":"Openswan 2.4.6",
	"^4f456c4c4f5d5264574e5244":"Openswan 2.4.6 X.509-1.5.4 LDAP_V3 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f454e7c454d716b5f4d6c67":"Openswan 2.4.6 X.509-1.5.4 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f457a7d6d6c5e5441727070":"Openswan 2.4.6rc3 X.509-1.5.4 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f4552756a414d79434d4951":"Openswan 2.4.7",
	"^4f455a7e4261425d725c705f":"Openswan 2.4.7 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f457a6d734b6f476273616c":"Openswan 2.4.8",
	"^4f455d62575860514272754c":"Openswan 2.4.8 LDAP_V3 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f4574514070784e717f5760":"Openswan 2.4.8 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f45414c5d6a75516450457a":"Openswan 2.4.9",
	"^4f45534a496f60726b636462":"Openswan 2.4.9 LDAP_V3 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f455f5d7b764b67436f4f49":"Openswan 2.4.9 PLUTO_SENDS_VENDORID PLUTO_USES_KEYRR",
	"^4f4546477e5e4b5440606859":"Openswan 2.5.0",
	"^4f45495c767449495c5a7350":"Openswan 2.5.00",
	"^4f457260466858434c7e6a45":"Openswan 2.5.01",
	"^4f45717a7c715b657c5c5156":"Openswan 2.5.02",
	"^4f456651517b4f475276654d":"Openswan 2.5.03",
	"^4f455672606d794f697d7242":"Openswan 2.5.04",
	"^4f454a4d5e5e674c604e4168":"Openswan 2.5.05",
	"^4f454a6176624e5876754d64":"Openswan 2.5.06",
	"^4f455c47464946434875464e":"Openswan 2.5.07",
	"^4f455a6f776e666c49497b68":"Openswan 2.5.08",
	"^4f454c4f577c5a7c4c665248":"Openswan 2.5.09",
	"^4f45714250575765766a6c72":"Openswan 2.5.10",
	"^4f457a795c6440407166776c":"Openswan 2.5.11",
	"^4f4549796c524b7c515b5450":"Openswan 2.5.12",
	"^4f45455740667a5f766d785d":"Openswan 2.5.13",
	"^4f45736b7f50645f6c416341":"Openswan 2.5.14",
	"^4f45675e407f696148444f7c":"Openswan 2.5.15",
	"^4f4557575d58474e5d574e58":"Openswan 2.5.16",
	"^4f457a74437b794a6148685b":"Openswan 2.5.17",
	"^4f455e74654a504c7a614967":"Openswan 2.5.18",
	"^4f45766b71776b6f48467a69":"Openswan 2.6.01",
	"^4f455f525758674a61465b6b":"Openswan 2.6.02",
	"^4f45775376797c60516a757b":"Openswan 2.6.03",
	"^4f45736f4c6569475a7d7f4c":"Openswan 2.6.04",
	"^4f457b654a44434170427663":"Openswan 2.6.05",
	"^4f454a4376414f737d6e495f":"Openswan 2.6.06",
	"^4f45466b5d7b4753765c686b":"Openswan 2.6.07",
	"^4f457d456755615659534c7b":"Openswan 2.6.08",
	"^4f455a447e4d547d6d416e6c":"Openswan 2.6.09",
	"^4f45744a61537c7646486641":"Openswan 2.6.10",
	"^4f455e7f4c79574b43455465":"Openswan 2.6.11",
	"^4f45775b5b5e5b705443404e":"Openswan 2.6.12",
	"^4f455a7f4b47466754526564":"Openswan 2.6.13",
	"^4f456f534a55776561714158":"Openswan 2.6.14",
	"^4f4563476e586e5f567a5457":"Openswan 2.6.15",
	"^4f456a7d637357765a5c7b63":"Openswan 2.6.16",
	"^4f4554704245584355764571":"Openswan 2.6.17",
	"^4f457d5a765a404d5b4f5744":"Openswan 2.6.18",
	"^4f456b71484c42504f664d44":"Openswan 2.6.19",
	"^4f4543714271574c644b7a41":"Openswan 2.6.20",
	"^4f454970424c6d5f4e5b6f59":"Openswan 2.6.20dr2",
	"^4f4550544259485a67464e66":"Openswan 2.6.20rc1",
	"^4f457e717f6b5a4e727d576b":"Openswan 2.6.21",
	"^4f456c6a405d72544d42754d":"Openswan 2.6.22",
	"^4f456d406b6753464548407f":"Openswan 2.6.23",
	"^4f45557d6068416e77737478":"Openswan 2.6.24",
	"^4f45694b5146645d6863434c":"Openswan 2.6.24rc3",
	"^4f45445743787f6f78467b4d":"Openswan 2.6.24rc5",
	"^4f4543606e547b776f5e5848":"Openswan 2.6.25",
	"^4f45504b7e7a764d4e645f57":"Openswan 2.6.26",
	"^4f456e544e77494c76567e5c":"Openswan 2.6.27",
	"^4f45517b4f7f6e657a7b4351":"Openswan 2.6.28",
	"^4f455e5a65725d6564727763":"Openswan 2.6.29",
	"^4f457656736b546968656675":"Openswan 2.6.30",
	"^4f457d476e447f5a4159655b":"Openswan 2.6.31",
	"^4f4568794c64414365636661":"Openswan 2.6.32",
	"^4f456768495f775c414c4679":"Openswan 2.6.33",
	"^4f457f7e637f7679517f4a5a":"Openswan 2.6.34",
	"^4f457e487a746b6f69705842":"Openswan 2.6.35",
	"^4f45716c74725d4b5a6c5d5f":"Openswan 2.6.36",
	"^4f45755c645c6a795c5c6170":"Openswan 2.6.37",
	"^4f4576795c6b677a57715c73":"Openswan 2.6.38",
	"^4f454b705270417f765b6b59":"Openswan 2.6.38dr2",
	"^4f45414f75405b4e6b554a50":"Openswan 2.6.38rc2",
	"^4f456d6470475f6c477d767d":"Openswan 2.6.39",
	"^4f456c4e75416271485b7970":"Openswan 2.6.39dr3",
	"^4f53577666617a6f6355505a":"Openswan 2.6.40",
	"^4f535773786c6a4640545359":"Openswan 2.6.41",
	"^4f535751624a50497c705f61":"Openswan 2.6.42",
	"^4f53577b5547416f4c674b64":"Openswan 2.6.43",
	"^4f53574745627352675b5a51":"Linux Openswan 2.6.44",
	"^4f53577e7b6566787577466d":"Linux Openswan 2.6.45",
	"^4f535771775064405e494145":"Linux Openswan 2.6.46",
	"^4f5357584f7a6d66706e7052":"Linux Openswan 2.6.47",
	"^4f53575353637b5979536b4c":"Linux Openswan 2.6.47.1",
	"^4f53576d77657d7c497e6c7c":"Linux Openswan 2.6.48",
	"^4f5357795f4472657a654753":"Linux Openswan 2.6.49",
	"^4f53575e5f45464d62615370":"Linux Openswan 2.6.50dev1",
	"^4f5357[[:xdigit:]]{18}$":"Openswan Unknown Vsn",
	"^4f454e574547444b6865684a":"Libreswan 3.3 LDAP_V3",
	"^4f454e5f52685050487b645e":"Libreswan 3.5",
	"^4f454e756f6b706a71757d5c":"Libreswan 3.5 LDAP_V3",
	"^4f454e[[:xdigit:]]{18}$":"FreeS/WAN or OpenSWAN or Libreswan",
	"^4f45[[:xdigit:]]{20}$":"FreeS/WAN or OpenSWAN",
	"^4f70656e504750":"OpenPGP",
	"^1d6e178f6c2c0be284985465450fe9d4":"FortiGate",
	"^299ee8289f40a8973bc78687e2e7226b532c3b76":"Netscreen-01",
	"^3a15e1f3cf2a63582e3ac82d1c64cbe3b6d779e7":"Netscreen-02",
	"^47d2b126bfcd83489760e2cf8c5d4d5a03497c15":"Netscreen-03",
	"^4a4340b543e02b84c88a8b96a8af9ebe77d9accc":"Netscreen-04",
	"^64405f46f03b7660a23be116a1975058e69e8387":"Netscreen-05",
	"^699369228741c6d4ca094c93e242c9de19e7b7c6":"Netscreen-06",
	"^8c0dc6cf62a0ef1b5c6eabd1b67ba69866adf16a":"Netscreen-07",
	"^92d27a9ecb31d99246986d3453d0c3d57a222a61":"Netscreen-08",
	"^9b096d9ac3275a7d6fe8b91c583111b09efed1a0":"Netscreen-09",
	"^bf03746108d746c904f1f3547de24f78479fed12":"Netscreen-10",
	"^c2e80500f4cc5fbf5daaeed3bb59abaeee56c652":"Netscreen-11",
	"^c8660a62b03b1b6130bf781608d32a6a8d0fb89f":"Netscreen-12",
	"^f885da40b1e7a9abd17655ec5bbec0f21f0ed52e":"Netscreen-13",
	"^2a2bcac19b8e91b426107807e02e7249569d6fd3":"Netscreen-14",
	"^166f932d55eb64d8e4df4fd37e2313f0d0fd8451":"Netscreen-15",
	"^a35bfd05ca1ac0b3d2f24e9e82bfcbff9c9e52b5":"Netscreen-16",
	"^9436e8d67174ef9aed068d5ad5213f187a3f8ba6":"Netscreen-16",
	"^4485152d18b6bbcc0be8a8469579ddcc":"avaya",
	"^c573b056d7faca36c2fba28374127cbf":"StoneGate-01",
	"^baeb239037e17787d730eed9d95d48aa":"StoneGate-02",
	"^526170746f7220506f77657256706e20536572766572205b56382e315d":"Symantec-Raptor-v8.1",
	"^526170746f7220506f77657256706e20536572766572":"Symantec-Raptor",
	"^..................54656c646174":"Teldat",
	"^bdb41038a7ec5e5534dd004d0f91f927":"Maybe Cisco IOS",
	"^edea53a3c15d45cafb11e59ea68db2aa99c1470e0000000400000303":"Unknown 3",
	"^bedc86dabf0ab7973870b5e6c4b87d3ee824de310000001000000401":"Unknown 4",
	"^ac5078c25cabb9523979978e76a3d0d2426bc9260000000400000401":"Unknown 5",
	"^69b761a173cc1471dc4547d2a5e94812":"Unknown 7",
	"^4c5647362e303a627269636b3a362e302e353732":"Unknown 8",
	"^3499691eb82f9eaefed378f5503671debd0663b4000000040000023c":"Unknown 9",
	"^975b7816f69789600dda89040576e0db":"Unknown 10",
	"^da8e9378":"Safenet or Watchguard",
	"^e23ae9f51a46876ff93d89ba725d649d":"Unknown-cisco",
	"^8404adf9cda05760b2ca292e4bff537b":"Maybe Sidewinder G2",
	"^e720cdd49d2ee7b83ce1970a6c69b528":"Maybe Sidewinder G2",
}
