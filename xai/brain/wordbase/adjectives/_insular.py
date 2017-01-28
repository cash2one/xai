

#calss header
class _INSULAR():
	def __init__(self,): 
		self.name = "INSULAR"
		self.definitions = [u'interested only in your own country or group and not willing to accept different or foreign ideas']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
