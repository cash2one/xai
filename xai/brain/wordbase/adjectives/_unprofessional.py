

#calss header
class _UNPROFESSIONAL():
	def __init__(self,): 
		self.name = "UNPROFESSIONAL"
		self.definitions = [u'not showing the standard of behaviour or skill that is expected of a person in a skilled job: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
