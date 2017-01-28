

#calss header
class _INGLORIOUS():
	def __init__(self,): 
		self.name = "INGLORIOUS"
		self.definitions = [u'that people should be ashamed of because it is not fair or honest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
