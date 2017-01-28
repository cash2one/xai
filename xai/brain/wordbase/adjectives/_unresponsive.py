

#calss header
class _UNRESPONSIVE():
	def __init__(self,): 
		self.name = "UNRESPONSIVE"
		self.definitions = [u'not reacting in a quick or positive way to something : ', u'not reacting or moving at all because of being unconscious or very ill : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
