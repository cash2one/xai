

#calss header
class _ALOOF():
	def __init__(self,): 
		self.name = "ALOOF"
		self.definitions = [u'not friendly or willing to take part in things: ', u'not interested or involved, usually because you do not approve of what is happening: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
