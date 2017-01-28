

#calss header
class _CLINICAL():
	def __init__(self,): 
		self.name = "CLINICAL"
		self.definitions = [u'used to refer to medical work or teaching that relates to the examination and treatment of ill people: ', u'expressing no emotion or feelings: ', u'showing no character and warmth: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
