

#calss header
class _REMOTE():
	def __init__(self,): 
		self.name = "REMOTE"
		self.definitions = [u'far away in distance or time, or not closely related: ', u'A remote area, house, or village is a long way from any towns or cities: ', u'remote computer systems are available to users in another part of a building or in another place, for example through a network: ', u'slight: ', u'not very friendly or showing little interest in other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
