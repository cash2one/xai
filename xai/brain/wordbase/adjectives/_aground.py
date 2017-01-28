

#calss header
class _AGROUND():
	def __init__(self,): 
		self.name = "AGROUND"
		self.definitions = [u'If a boat or ship is aground, it is unable to move because it is touching ground or in a place where there is very little water: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
