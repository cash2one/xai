

#calss header
class _SUBJECT():
	def __init__(self,): 
		self.name = "SUBJECT"
		self.definitions = [u'to have or experience a particular thing, especially something unpleasant: ', u'only able to happen if something else happens: ', u'under the political control of another country or state: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
