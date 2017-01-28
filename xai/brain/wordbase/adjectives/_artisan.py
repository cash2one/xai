

#calss header
class _ARTISAN():
	def __init__(self,): 
		self.name = "ARTISAN"
		self.definitions = [u'made in a traditional way by someone who is skilled with their hands: ', u'making things in a traditional way with your hands: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
