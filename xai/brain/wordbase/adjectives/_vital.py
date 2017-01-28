

#calss header
class _VITAL():
	def __init__(self,): 
		self.name = "VITAL"
		self.definitions = [u'necessary for the success or continued existence of something; extremely important: ', u'energetic: ', u'relating to life']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
