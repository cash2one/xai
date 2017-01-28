

#calss header
class _INCONSISTENT():
	def __init__(self,): 
		self.name = "INCONSISTENT"
		self.definitions = [u'If a reason, idea, opinion, etc. is inconsistent, different parts of it do not agree, or it does not agree with something else: ', u'not staying the same in behaviour or quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
