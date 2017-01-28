

#calss header
class _PRACTICAL():
	def __init__(self,): 
		self.name = "PRACTICAL"
		self.definitions = [u'relating to experience, real situations, or actions rather than ideas or imagination: ', u'in fact: ', u'suitable for the situation in which something is used: ', u'able to provide effective solutions to problems: ', u'able to be done or put into action: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
